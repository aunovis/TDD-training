using System;
using System.Text;

namespace MarsRover
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.UTF8;

            var rover = new Rover(5, 5, Direction.North);
            var world = new World(20, 20);
            world.Obstacles.Add((8, 8));
            rover.LandOn(world);
            rover.Execute(new[] { 'f' });

            char key;
            do
            {
                key = Console.ReadKey().KeyChar;

                Console.Clear();

                try
                {
                    switch (key)
                    {
                        case 'a':
                            rover.Execute(new[] {'l'});
                            break;
                        case 'w':
                            rover.Execute(new[] {'f'});
                            break;
                        case 's':
                            rover.Execute(new[] {'b'});
                            break;
                        case 'd':
                            rover.Execute(new[] {'r'});
                            break;
                    }
                    Console.BackgroundColor = ConsoleColor.Black;
                }
                catch (ObstacleException)
                {
                    Console.BackgroundColor = ConsoleColor.Red;
                    //Console.WriteLine("GAME OVER");
                    //key = 'x';
                }
            } while (key != 'x');

        }
    }
}
