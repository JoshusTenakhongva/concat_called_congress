import requests, json, os

def main(): 
    # Initialization
    propublica_key= os.getenv( 'propub_key' )
    propub_header= { 'X-API-Key':propublica_key }
    propub_params= { 'congress': 117, 'chamber': 'senate' }
    propub_base= 'https://api.propublica.org/congress/v1/117/senate'

    regulations_key= os.getenv( 'reg_key' )
    reg_headers= {'X-Api-Key': regulations_key, 'Content-Type': 'application/vnd.api+json' }
    reg_params= {}
    reg_base= 'https://api.regulations.gov/v4/documents'

    openfec_key= os.getenv( 'fec_key' )
    fec_params= {'api_key': openfec_key, 'q': 'erik aadland' }
    fec_base= 'https://api.open.fec.gov/v1'
    fec_query= '/candidates/search/'

    propublica_r= requests.get( propub_base, headers=propub_header, params=propub_params )
    regulations_r= requests.get( reg_base, headers=reg_headers ) 
    openfec_r= requests.get( fec_base+fec_query, params=fec_params )

    print( 'proPublica: ' + str(propublica_r.status_code) )
    print( 'regulations: ' + str(regulations_r.status_code) )
    print( 'open fec: ' + str(openfec_r.status_code) )

    # Save response

def write_json( filename, content ): 

    with open( filename, 'w' ) as outfile: 
        json.dump( content, outfile )

if __name__ == "__main__": 
    main()