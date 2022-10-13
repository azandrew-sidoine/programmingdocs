using System;
using System.IO;


namespace FileSystem
{
    class Program
    {
        static void Main(string[] args)
        {
            var _nestedFoldersPath = Path.Combine("TestFolders", "TestSubFolder");

            Console.WriteLine($"Creating Directory {_nestedFoldersPath.ToString()}");

            Directory.CreateDirectory(_nestedFoldersPath);

            Console.WriteLine("Created Folders");

            Console.WriteLine($"{Environment.SpecialFolder.ApplicationData}");

            Console.WriteLine($"{Environment.SpecialFolder.LocalApplicationData}");

        }
    }
}
