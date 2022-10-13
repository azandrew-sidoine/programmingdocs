using System;

namespace TestApplication
{
    public class MethodOverloadClass
    {
        public void CallMethod()
        {
            Console.WriteLine("Method 1");
        }

        public void CallMethod(int param1, int? param2 = null, int? param3 = null)
        {
            Console.WriteLine("Method 3");
        }

        public void CallMethod(int param1, int? param2 = null)
        {
            Console.WriteLine("Method 2");
        }
    }
}
