import pickle
import os

# Method 1: Basic way to read a pickle file
def read_pickle_basic(file_path):
    """
    Basic method to read a pickle file
    """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# Method 2: With error handling
def read_pickle_safe(file_path):
    """
    Safe method to read a pickle file with error handling
    """
    try:
        if not os.path.exists(file_path):
            print(f"File {file_path} does not exist.")
            return None
            
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        print(f"Successfully loaded pickle file: {file_path}")
        return data
        
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except pickle.UnpicklingError:
        print(f"Error unpickling file {file_path}. File may be corrupted.")
        return None
    except Exception as e:
        print(f"Unexpected error reading {file_path}: {str(e)}")
        return None

# Method 3: Inspect pickle file contents
def inspect_pickle_file(file_path):
    """
    Inspect the contents of a pickle file
    """
    data = read_pickle_safe(file_path)
    
    if data is not None:
        print(f"\nFile: {file_path}")
        print(f"Data type: {type(data)}")
        
        if isinstance(data, (list, tuple)):
            print(f"Length: {len(data)}")
            if len(data) > 0:
                print(f"First element type: {type(data[0])}")
                print(f"First few elements: {data[:3]}")
                
        elif isinstance(data, dict):
            print(f"Keys: {list(data.keys())}")
            print(f"Number of items: {len(data)}")
            
        elif hasattr(data, 'shape'):  # For numpy arrays, pandas DataFrames
            print(f"Shape: {data.shape}")
            
        else:
            print(f"Content preview: {str(data)[:200]}...")
            
    return data

# Example usage
if __name__ == "__main__":
    file_path = 'metadata.pkl'
    
    # Method 1: Basic usage
    # data = read_pickle_basic(file_path)
    
    # Method 2: Safe usage (recommended)
    data = read_pickle_safe(file_path)
    
    # Method 3: Inspect the file
    # data = inspect_pickle_file(file_path)
    
    # Work with your data
    if data is not None:
        print("Data loaded successfully!")
        # Process your data here
        print(f"Data type: {type(data)}")
        print(data[0])
