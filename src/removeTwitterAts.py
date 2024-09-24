import pandas as pd
import re

def remove_twitter_handles_and_links(input_csv, output_csv):
    # Read the CSV file
    df = pd.read_csv(input_csv)

    # Define a function to remove Twitter handles and links from a string
    def clean_text(text):
        if isinstance(text, str):  # Check if the input is a string
            # Remove Twitter handles
            text = re.sub(r'@\w+', '', text)
            # Remove URLs
            text = re.sub(r'http[s]?://\S+', '', text)
            text = re.sub(r'www\.\S+', '', text)
            return text.strip()  # Remove leading/trailing whitespace
        return text

    # Apply the function to each column in the DataFrame
    df_cleaned = df.map(clean_text)

    # Save the cleaned DataFrame to a new CSV file
    df_cleaned.to_csv(output_csv, index=False)

# Example usage
input_file = '../elon_musk_tweets.csv'  # Replace with your input file name
output_file = 'output.csv'  # Replace with your desired output file name
remove_twitter_handles_and_links(input_file, output_file)