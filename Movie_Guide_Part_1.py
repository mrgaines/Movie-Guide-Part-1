#Jay Gaines
#CIS261

def movie_guide():
    print("The Movie Guide Application")
    print()
    print("Command Menu")
    print("list ---> List all the movies")
    print("add ----> Add a movie title")
    print("delete ----> Delete a Movie title")
    print("exit ---> Close the Application")
    
def list(movie_list):
    for i, movie in enumerate(movie_list, start = 1):
        print(f"{i}. {movie}")
        print()
        
def add(movie_list):
    movie = input("Name: ")
    movie_list.append(movie)
    print(f"{movie} was added. \n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number. \n")
    else:
        movie = movie_list.pop(number - 1)
        print(f"{movie} was deleted. \n")
        
def main():
    movie_list = ["Batman", "Saw", "Aquaman"]
    movie_guide()
    while True:
        command = input("Enter Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "delete":
            delete(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command, please try again")
            
    print("Later or Goodbye")
    
if __name__ == "__main__":
    main()
    
        

