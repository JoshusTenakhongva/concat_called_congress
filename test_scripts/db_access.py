import psycopg 

def psql_connect( cred ): 
    # Init
    with psycopg.connect( cred ) as conn: 
        print( 'connected' )