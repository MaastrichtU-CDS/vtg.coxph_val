""" methods.py

This file contains all algorithm pieces that are executed on the nodes.
It is important to note that the master method is also triggered on a
node just the same as any other method.

When a return statement is reached the result is send to the central
server after encryption.
"""
import os
import sys
import time
import json
import pandas

from vantage6.tools.util import info, warn
import coxph_validate.concordance_index as ci
import coxph_validate.org_id as do
import coxph_validate.apply_filters as af


def master(client,data,org_ids,betas,time_col,censor_col, filter_data):#,#betas,time_col,censor_col):
    """Master algoritm.

    The master algorithm is the chair of the Round Robin, which makes
    sure everyone waits for their turn to identify themselfs.
    """

    # get all organizations (ids) that are within the collaboration
    # FlaskIO knows the collaboration to which the container belongs
    # as this is encoded in the JWT (Bearer token)
    #organizations = client.get_organizations_in_my_collaboration()
    #ids = [organization.get("id") for organization in organizations]

    ids = org_ids

    # The input fot the algorithm is the same for all organizations
    # in this case
    info("Defining input parameters")
    input_ = {
        "method": "validate",
        "kwargs":{
                "betas": betas,
                "time_col": time_col,
                "censor_col": censor_col,
                "filter": filter_data
            }
        }
    

    # create a new task for all organizations in the collaboration.
    info("Dispatching node-tasks")
    task = client.create_new_task(
        input_=input_,
        organization_ids=ids
    )

    # wait for node to return results. Instead of polling it is also
    # possible to subscribe to a websocket channel to get status
    # updates
    info("Waiting for results")
    task_id = task.get("id")
    task = client.get_task(task_id)
    while not task.get("complete"):
        task = client.get_task(task_id)
        info("Waiting for results")
        time.sleep(1)

    info("Obtaining results")
    results_master = client.get_results(task_id=task.get("id"))
    organization_ids = []
    result_ci = []
    result_org_id=[]

    try:
        for results in results_master:
            if results['flag']==1:
                organization_ids.append(results['Org id'])
            else:
                result_ci.append(results['Concordance Index'])
                result_org_id.append(results['Org id'])
    

        if organization_ids:
            message_from_master={'Organization ids uncompleted task':organization_ids}
    
        if len(result_ci) == len(org_ids) & len(result_org_id)==len(org_ids):
            Mean_ci = sum(result_ci)/len(result_ci)
            ind_ci=list(zip(result_ci,result_org_id))
            message_to_server = {
                'Mean Concordance Index':Mean_ci,
                'Concordance Indexes':ind_ci            
            }
        else:
            message_to_server={
                'Concordance Indexes Not Calculated for':organization_ids,
            }    
    except Exception as e:
        message_to_server={'Exception':e}

    #results = [json.loads(result.get("result")) for result in results]
    #average all the results
    #message_to_server = {'results':results_master}

    info("master algorithm complete")

    # return all the messages from the nodes
    return message_to_server

def RPC_validate(data,betas,time_col,censor_col,filter): #,#betas,time_col,censor_col)
    """Some_example_method.

    loads the dataframe and reports if it succeeded by returning a
    boolean value.
    """

    client_node = do.temp_fix_client()
    org_id = do.find_my_organization_id(client_node)

    data_f = af.apply_filter_atomcat(data,filter)

    #Check if data_f is empty
    if len(data_f.columns) == 0:
        print("Dataframe is empty")
        
        message_to_server={'Concordance Index': "result not calculated",
                           'Dataframe':'empty',
                            'Org id':org_id,
                            'flag':1}
    else:

        try:
            result = ci.c_index(data_f,betas,time_col,censor_col)
            message_to_server={'Concordance Index': result,
                            'Org id':org_id,
                            'flag':0}
        except Exception as e: 
            message_to_server={'Concordance Index': "result not calculated",
                            'Org id':org_id,
                            "Exception":e,
                            'flag':1}

    return message_to_server
