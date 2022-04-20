import requests, json, os

def main(): 
    # Initialization
    propublica_key= os.getenv( 'propub_key' )
    propub_params= {'X-API-key': propublica_key }
    propub_base= 'https://api.propublica.org/congress/v1'

    regulations_key= os.getenv( 'reg_key' )
    reg_params= {'X-Api-Key': regulations_key, 'Content-Type': 'application/vnd.api+json' }
    reg_base= 'https://api.regulations.gov/v4/documents'

    openfec_key= os.getenv( 'fec_key' )
    fec_params= {'api_key': openfec_key }
    fec_base= 'https://api.open.fec.gov/v1'
    fec_query= '/candidates/search/erik aadland/'

    #propublica_r= requests.get( )
    #regulations_r= requests.get() 
    openfec_r= requests.get( fec_base+fec_query, params=fec_params )
    write_json( 'fec.json', openfec_r.json() ) 

    # Construct API Request
    #response = requests.get(state_url)

    # Save response

def write_json( filename, content ): 

    with open( filename, 'w' ) as outfile: 
        json.dump( content, outfile )

if __name__ == "__main__": 
    main()