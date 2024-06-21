import csv

# writes the post information to a csv file
def write_to_csv(post_info, filename='posts.csv'):
    # Define the column names
    fieldnames = ['Author', 'Author Profile Link', 'Post Link']

    # Open the file in write mode
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the job details
        for job in post_info:
            writer.writerow(job)

    print(f"Data written to {filename} successfully.")