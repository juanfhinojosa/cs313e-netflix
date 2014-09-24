from Netflix import Netflix_Solve
global_id = ''
input_file = open("Run.Netflix.in.txt", "r")
output_file = open("Run.Netflix.out.txt", "a")

Netflix_Solve(input_file, output_file)

input_file.close()
output_file.close()