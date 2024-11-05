# test_weaviate.py

import logging
import uuid
from aeiva.storage.weaviate.weaviate_database import WeaviateDatabase  # Adjust the import as necessary
from aeiva.storage.weaviate.weaviate_config import WeaviateConfig  # Adjust the import as necessary

# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    # Configuration for Weaviate
    weaviate_config = WeaviateConfig(
        url='http://localhost:8080',  # Replace with your Weaviate URL
        api_key=None,                 # Provide API key if required
        auth_client_secret=None,      # Provide auth client secret if using OIDC
        index_name='MyIndex',
        vector_dim=128,               # Adjust according to your vector dimensions
        distance_metric='cosine',     # 'cosine', 'l2-squared', or 'dot'
    )
    config_dict = weaviate_config.to_dict()

    # Initialize Weaviate vector store
    weaviate_store = WeaviateDatabase(config=config_dict)

    try:
        # Prepare sample data
        vector_dimension = weaviate_config.vector_dim
        vectors = [
            [float(i) for i in range(vector_dimension)],  # Sample vector 1
            [float(i + 1) for i in range(vector_dimension)],  # Sample vector 2
        ]
        payloads = [
            {'name': 'Vector 1', 'description': 'First test vector.'},
            {'name': 'Vector 2', 'description': 'Second test vector.'},
        ]
        ids = [str(uuid.uuid4()), str(uuid.uuid4())]  # Generate unique IDs

        # Insert vectors into the collection
        weaviate_store.insert_vectors(
            collection_name=weaviate_config.index_name,
            vectors=vectors,
            payloads=payloads,
            ids=ids
        )
        logging.info(f"Inserted vectors with IDs: {ids}")

        # Search for similar vectors
        query_vector = [float(i + 0.5) for i in range(vector_dimension)]  # Query vector
        search_results = weaviate_store.search_vectors(
            collection_name=weaviate_config.index_name,
            query_vector=query_vector,
            top_k=2
        )
        print(f"Search results:\n{search_results}")

        # Retrieve a specific vector
        vector_id = ids[0]
        retrieved_vector = weaviate_store.get_vector(
            collection_name=weaviate_config.index_name,
            vector_id=vector_id
        )
        print(f"Retrieved vector:\n{retrieved_vector}")

        # Update a vector's payload
        new_payload = {'name': 'Vector 1 Updated', 'description': 'Updated description.'}
        weaviate_store.update_vector(
            collection_name=weaviate_config.index_name,
            vector_id=vector_id,
            payload=new_payload
        )
        logging.info(f"Updated vector with ID: {vector_id}")

        # Retrieve the updated vector
        updated_vector = weaviate_store.get_vector(
            collection_name=weaviate_config.index_name,
            vector_id=vector_id
        )
        print(f"Updated vector:\n{updated_vector}")

        # Delete a vector
        weaviate_store.delete_vector(
            collection_name=weaviate_config.index_name,
            vector_id=vector_id
        )
        logging.info(f"Deleted vector with ID: {vector_id}")

        # Attempt to retrieve the deleted vector
        try:
            deleted_vector = weaviate_store.get_vector(
                collection_name=weaviate_config.index_name,
                vector_id=vector_id
            )
            print(f"Deleted vector:\n{deleted_vector}")
        except KeyError as e:
            logging.info(f"Vector with ID {vector_id} has been deleted and cannot be retrieved.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Close the connection
        del weaviate_store

if __name__ == '__main__':
    main()