using System;
using System.Collections.Generic;
using System.Text;

namespace MarsRover
{
    public class ConsoleOutput : IOutput
    {
        public ConsoleOutput()
        {
            Console.OutputEncoding=Encoding.UTF8;
        }

        public void Print(World world)
        {
            for (int y = 0; y< world.Dimension.y;y++)
            {
             Console.WriteLine("\u2591");   
            }
        }

        public void Render()
        {
            throw new NotImplementedException();
        }
    }
}
