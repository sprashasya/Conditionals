# Movie Rating: Determine if a person can watch a movie based on their age and the movie's rating (G, PG, PG-13, R).
movie_grading=input(("enter the grading of movie:\n"))

if movie_grading.isdigit():
    print(f"The input '{movie_grading}' is not a string.")
    print("Please enter the valid details")
    exit()


if movie_grading=="G":
    Age_Suitability="Suitable for everyone, including young children. No age restriction."
    content="Movies are wholesome with no objectionable content. They're safe for family viewing."

elif movie_grading=="PG":
    Age_Suitability="Children under 10 should watch with a parent or guardian."
    content="Might have mild language, brief nudity, or mild violence that parents might want to explain to younger kids."

elif movie_grading=="PG-13":
    Age_Suitability="Not recommended for children under 13. Parents should decide if it's okay for their teens."
    content="Could include moderate language, some violence, and themes that might not be suitable for younger kids."

elif movie_grading=="R":
    Age_Suitability="Restricted to viewers over 17 (18 in some places). Younger teens need an adult to watch with them."
    content="Often has strong language, intense violence, explicit scenes, or mature themes not suitable for younger audiences."
else:
    print("You Have given wrong grading")

print("Age Recommendation:",Age_Suitability,"Content:",content)