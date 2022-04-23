import requests, json, os
from dotenv import dotenv_values

def main(): 
    # Initialization
    e_var= dotenv_values( '.env' )

    # Set up requests, headers, and parameters
    propublica_key= e_var[ 'propub_key' ]
    propub_header= { 'X-API-Key':propublica_key }
    propub_params= {}
    propub_base= 'https://api.propublica.org/congress/v1/117/nominees/confirmed.json'

    regulations_key= e_var[ 'reg_key' ]
    reg_headers= {'X-Api-Key':regulations_key, 'Content-Type':'application/vnd.api+json' }
    reg_params= {}
    reg_base= 'https://api.regulations.gov/v4/documents'

    openfec_key= e_var[ 'fec_key' ]
    fec_params= {'api_key':openfec_key, 'q':'erik aadland' }
    fec_base= 'https://api.open.fec.gov/v1'
    fec_query= '/candidates/search/'

    # Send requests
    propublica_r= requests.get( propub_base, headers=propub_header, params=propub_params )
    regulations_r= requests.get( reg_base, headers=reg_headers ) 
    openfec_r= requests.get( fec_base+fec_query, params=fec_params )

    # Check status codes
    print( 'proPublica: ' + str(propublica_r.status_code) )
    print( 'regulations: ' + str(regulations_r.status_code) )
    print( 'open fec: ' + str(openfec_r.status_code) )

    # Save response in Json format
    write_json( 'propublica.json', propublica_r.json() )
    write_json( 'regulations.json', regulations_r.json() )
    write_json( 'openfec.json', openfec_r.json() )

    # Close responses
    propublica_r.close()
    regulations_r.close()
    openfec_r.close() 


def write_json( filename, content ): 

    with open( filename, 'w' ) as outfile: 
        json.dump( content, outfile )

if __name__ == "__main__": 
    main()