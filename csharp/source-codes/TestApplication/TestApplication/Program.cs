using System;

namespace TestApplication
{
    class Program
    {
        static void Main(string[] args)
        {
            var obj = new MethodOverloadClass();

            obj.CallMethod(0, null);
        }
    }
}
