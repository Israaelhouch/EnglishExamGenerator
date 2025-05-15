from backend.src.routes.exam_generator import generate_exam

def main():
    chapter, result = generate_exam(2)
    print ("Chapter: ",chapter)
    print("\n")
    print (result)

if __name__ == "__main__":
    main()