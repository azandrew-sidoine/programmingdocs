# .NET Filesystems


```cs
[HttpPost, DisableRequestSizeLimit]
public async Task<IActionResult> Upload()
{
    try
    {
        var formCollection = await Request.ReadFormAsync();
        var file = formCollection.Files.First();
    } catch (Exception e) {

    }
    // ...
}
```

Note: `System.IO` namespace contains most of classes for working with I/O based operations.

Note: `@` operator in dotnet

> @ - It's useful when working with Pattern and String as it converts characters into unicode and helps not to escape unicode character.

Note: OS Environment:

> `Environment.NewLine` - Returns the new line character for the OS.
> `Environment.SpecialFolder.ApplicationData` - Returns the ApplicationData folder
> `Environment.SpecialFolder.LocalApplicationData` - Returns the Local application data folder.

## Working with Directory class

> `System.IO.Directory.CreateDirectory(path) -> DirectoryInfo` - Create the directory for path relative to executable. It Overrides any directory with the same name.

> `Directory.Exists(path) -> bool` - Returns boolean indicating whether directory exist or not.

> Directory.Delete(string <Path>, bool <Recursive>) - Remove a directory from the file system. recursive flags tells the directory class to recusively remove the directory

> Directory.GetDirectories(string <Path>) -> string[] - Returns the list of directories in a given directory.

> Directory.GetFiles(string <Path>)  -> string[] - Returns the list of files in a given directory.

> Directory.GetDirectoryRoot(string path) -> string - Return the directory root of a path.

> Directory.GetFileSystemEntries(string <Path>) -> string[] - Returns the list of folders and directory in a path.

```cs
using System.IO;

namespace Namespace
{
    public class Program
    {
        const TestDirectory = "Test Folder";
        const NestedFoldersPath = Path.Combine("TestFolders", "TestSubFolder");
        public static void Main(string[] args)
        {

        }

        public static WorkingWithDirectory()
        {
            // Check if directory exists
            if (Directory.Exists(TestDirectory)) {
                // Directory already exists
            }

            // Creating directories
            Directory.CreateDirectory(TestDirectory);
            Direcory.CreateDirectory(NestedFoldersPath);

            if (Directory.Exists(TestDirectory)) {
                // Deleting Directory
                Directory.Delete(TestDirectory, true);
            }

            // Copying/Moving folders
            if (Directory.Exists(TestDirectory)) {
                // Deleting Directory
                Directory.Move(TestDirectory, $"{DstDirectory}_{DateTime.Now.ToString(\"yyyyMMddHHmmss"\)}");
            }
        }
    }
}
```

## Files I/O operations

File Modes:

```cs
public enum FileMode
{
    CreateNew = 1,
    Create = 2,
    Open = 3,
    OpenOrCreate = 4,
    Truncate = 5,
    Append = 6
}
```

> File.WriteAllText(string <Path>, string <InputData>) - Write data to file in text mode

> new FileInfo(string path) - Return a file information object pointer to a string path

> fileInfo.Name -> string - Name of the file being referenced

> fileInfo.Extension -> string - Extension of the file being referenced

> fileInfo.Length -> Int - Return the number of bytes in a file

> fileInfo.FullName -> string - Returns the full path to the file

> File.WriteAllLines(string <Path>, List<string> arr) - Write to a file with each line being an entry in the `arr` parameter.

> File.ReadAllLines(string <Path>) -> List<string> - Read the content of a file into a list of string.

> File.Copy(string <SourcePath>, string <DestinationPath>) - Copy the content from a path to another.

> File.Move(string <SourcePath>, string <DestinationPath>) - Move the content from a path to another.

>  new FileStream(string <Path>, FileMode <mode>="FileMode.Create|etc...") - Create an instance of a file stream class

> fs.CopyTo() - Copy a file to new content

> File.Open(string <Path>[, FileMode <mode>] [, FileAccess <access>] [, FileShare <share>]) -> FileStream - Create a file stream object by opening the file

> File.ReadAllBytesAsync(string <Path>[, CancellationToken <cancellationToken = default>]) -> Task<byte[]> - Read all bytes async

> File.WriteAllBytesAsync(string <Path>[, CancellationToken <cancellationToken = default>]) -> Task<byte[]> - Write all bytes async. Returns the number of written bytes.

```cs
using System.IO;

namespace Namespace
{
    public class Program
    {
        const TestDirectory = "Test Folder";
        const TestFilePath = Path.Combine(TestDirectory, "TestSubFolder.txt");
        public static void Main(string[] args)
        {

        }

        public static WorkingWithFiles()
        {
            var value = new FileInfo(TestFilePath);

            // Get the filename 
            var name = value.Name;

            // Get Extension
            var ext = value.Extension;

            // Get size of file in bytes
            var size = value.Length;

            // Creating a file
            if (!File.Exists(TestFilePath)) {
                // Create file from array input
                File.WriteAllLines(TestFilePath, []);
            }

            // Reading data from a file
            var lines = File.ReadAllLines(TestFilePath);

            // Working with Bynary types
        }
    }
}
```

## Paths

> Path.GetFileName(string <PathToFile>) - Return file name from a full file path.

> Path.DirectorySeparatorChar - Returns the directory separator character based on the file system

> Path.GetDirectoryName(string <Path>) - Return the base directory name of the path.

## Memory Stream class

```cs
using System;
using System.IO;
using System.Text;

class MemStream
{
    static void Main()
    {
        int count;
        byte[] byteArray;
        char[] charArray;
        UnicodeEncoding uniEncoding = new UnicodeEncoding();

        // Create the data to write to the stream.
        byte[] firstString = uniEncoding.GetBytes(
            "Invalid file path characters are: ");
        byte[] secondString = uniEncoding.GetBytes(
            Path.GetInvalidPathChars());

        using(MemoryStream memStream = new MemoryStream(100))
        {
            // Write the first string to the stream.
            memStream.Write(firstString, 0 , firstString.Length);

            // Write the second string to the stream, byte by byte.
            count = 0;
            while(count < secondString.Length)
            {
                memStream.WriteByte(secondString[count++]);
            }

            // Write the stream properties to the console.
            Console.WriteLine(
                "Capacity = {0}, Length = {1}, Position = {2}\n",
                memStream.Capacity.ToString(),
                memStream.Length.ToString(),
                memStream.Position.ToString());

            // Set the position to the beginning of the stream.
            memStream.Seek(0, SeekOrigin.Begin);

            // Read the first 20 bytes from the stream.
            byteArray = new byte[memStream.Length];
            count = memStream.Read(byteArray, 0, 20);

            // Read the remaining bytes, byte by byte.
            while(count < memStream.Length)
            {
                byteArray[count++] =
                    Convert.ToByte(memStream.ReadByte());
            }

            // Decode the byte array into a char array
            // and write it to the console.
            charArray = new char[uniEncoding.GetCharCount(
                byteArray, 0, count)];
            uniEncoding.GetDecoder().GetChars(
                byteArray, 0, count, charArray, 0);
            Console.WriteLine(charArray);
        }
    }
}
```
