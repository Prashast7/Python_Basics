import pandas as pd
import os

# Function to create partitions and save Parquet files inside subject folders
def create_partitions(input_csv, output_dir):
    # Step 1: Read the CSV file
    df = pd.read_csv(input_csv)
    
    # Step 2: Ensure the 'subject' column exists
    if 'subject' not in df.columns:
        raise ValueError("CSV does not contain a 'subject' column")
    
    # Step 3: Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Step 4: Create partitions by subject
    subjects = df['subject'].unique()  # Get unique subjects
    for subject in subjects:
        # Step 5: Filter rows for each subject
        partition_df = df[df['subject'] == subject]
        
        # Step 6: Create a new folder for each subject inside the main output directory
        subject_folder = os.path.join(output_dir, f'subject={subject}')
        if not os.path.exists(subject_folder):
            os.makedirs(subject_folder)
        
        # Step 7: Save partition as a Parquet file inside the subject folder
        partition_file_parquet = os.path.join(subject_folder, f'{subject}.parquet')
        partition_df.to_parquet(partition_file_parquet, index=False, engine='pyarrow')
        print(f"Partition for subject '{subject}' saved to: {partition_file_parquet}")

# Example usage
input_csv = r'C:\Users\Administrator\Desktop\students_with_header.csv'  # Specify the path to your input CSV
output_dir = r'C:\Users\Administrator\Desktop\students_partitions'  # Specify the directory to save the partitions

create_partitions(input_csv, output_dir)
