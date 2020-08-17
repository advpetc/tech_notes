**Compare two Files containing two integer**

>Complete the method below to read two integers
from the input file, compare them, and write true or false into the output file based on
whether the values are the same or not.

```java
// inputFile: path to input file; outputFile: path to output file
public void compareValues(String inputFile, String outputFile) {
  Scanner scan = null;
  PrintWriter pw = null;
  try {
    scan = new Scanner(new FileReader(inputFile));
    int num1 = scan.nextInt();
    int num2 = scan.nextInt();
    pw = new PrintWriter(new FileWriter(outputFile));
    if (num1 == num2) {
      pw.println("true");
    } else {
      pw.println("false");
    }
  } catch (FileNotFoundException fnfe) {
    System.out.println("fnfe: " + fnfe.getMessage());
  } catch (IOException ioe) {
    System.out.println("ioe: " + ioe.getMessage());
  } finally {
    if (pw != null) {
    pw.close();
    }
    if (scan != null) {
    scan.close();
    }
  }
}

```

**Scanner** takes in a **FileReader** instannce
**FileReader** takes in a path string

##ChatRoom Practice -- Serialization in network

1. main thread for connection, and each thread with each client
2. `PrintWriter` for printing string

