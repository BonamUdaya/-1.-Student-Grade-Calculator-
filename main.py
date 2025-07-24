System.out.print("Enter student name: ");
    String name = sc.nextLine();

    System.out.print("Enter marks in Math: ");
    int math = sc.nextInt();
    System.out.print("Enter marks in Science: ");
    int science = sc.nextInt();
    System.out.print("Enter marks in English: ");
    int english = sc.nextInt();

    double average = (math + science + english) / 3.0;
    String grade;

    if (average >= 90) grade = "A+";
    else if (average >= 80) grade = "A";
    else if (average >= 70) grade = "B";
    else if (average >= 60) grade = "C";
    else grade = "Fail";

    System.out.println("\n--- Student Report ---");
    System.out.println("Name: " + name);
    System.out.println("Average Marks: " + average);
    System.out.println("Grade: " + grade);
}
