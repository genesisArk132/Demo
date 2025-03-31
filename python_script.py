# Program to print values in 1000 count
import random

def generate_shuffled_ids(num_ids, num_outputs):
  """Generates a list of shuffled IDs and returns a specified number of outputs.

  Args:
    num_ids: The number of IDs to shuffle (e.g., 50).
    num_outputs: The number of shuffled IDs to return (e.g., 1000).

  Returns:
    A list of shuffled IDs.
  """

  ids = [f"svr_{i:02d}" for i in range(1, num_ids + 1)] #creates the list of id's
  shuffled_ids = []

  for _ in range(num_outputs):
    shuffled_ids.extend(random.sample(ids, len(ids))) #shuffles the list and extends the output list

  return shuffled_ids[:num_outputs] #returns the number of requested outputs.

# Example usage:
output_ids = generate_shuffled_ids(50, 1000)

for i in range(10): #print out the first 10.
  print(output_ids[i])

print(f"Total number of output IDs: {len(output_ids)}")
