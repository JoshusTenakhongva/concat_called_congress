import requests, json, os
from dotenv import dotenv_values
import db_access

def main(): 
    # Initialization
    e_var= dotenv_values( '.env' )

    

    


def write_json( filename, content ): 

    with open( filename, 'w' ) as outfile: 
        json.dump( content, outfile )

def propub_pull( e_var ): 
    # Set up requests, headers, and parameters
    propublica_key= e_var[ 'propub_key' ]
    propub_header= { 'X-API-Key':propublica_key }
    propub_params= {}
    propub_base= 'https://api.propublica.org/congress/v1/117/nominees/confirmed.json'

    # Send requests
    propublica_r= requests.get( propub_base, headers=propub_header, params=propub_params )

    # Check status codes
    print( 'proPublica: ' + str(propublica_r.status_code) )

    # Save response in Json format
    write_json( 'propublica.json', propublica_r.json() )

    # Close responses
    propublica_r.close()

    # Return our response in json format
    return propublica_r.json() 

def regulations_pull( e_var ): 
    # Init

    # Set up requests, headers, and parameters
    regulations_key= e_var[ 'reg_key' ]
    reg_headers= {'X-Api-Key':regulations_key, 'Content-Type':'application/vnd.api+json' }
    reg_params= {}
    reg_base= 'https://api.regulations.gov/v4/documents'

    # Send requests
    regulations_r= requests.get( reg_base, headers=reg_headers ) 

    # Check status codes
    print( 'regulations: ' + str(regulations_r.status_code) )

    # Save response in Json format
    write_json( 'regulations.json', regulations_r.json() )

    # Close responses
    regulations_r.close()

    # Return our response in json format
    return regulations_r.json()

def fec_pull( e_var ): 
    # Init

    # Set up requests, headers, and parameters
    openfec_key= e_var[ 'fec_key' ]
    fec_params= {'api_key':openfec_key, 'q':'erik aadland' }
    fec_base= 'https://api.open.fec.gov/v1'
    fec_query= '/candidates/search/'

    # Send requests
    openfec_r= requests.get( fec_base+fec_query, params=fec_params )

    # Check status codes
    print( 'open fec: ' + str(openfec_r.status_code) )

    # Save response in Json format
    write_json( 'openfec.json', openfec_r.json() )

    # Close responses
    openfec_r.close() 

    # Return our response in json format
    return openfec_r.json()
    
    

if __name__ == "__main__": 
    main()