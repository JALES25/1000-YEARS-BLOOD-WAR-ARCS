// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Main program; currently not implemented

using System;

namespace S1P1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hellaru tZu ZAwaru!");

            //Create a new car object using the default constrctor
            Car car1 = new Car();
            car1.UID = "car101";
            car1.Make = "Toyota";
            car1.Model = "Camly";
            car1.Year = 2021;
            car1.NumDoors = 4;
            car1.BodyStyle = "Sedan";
            car1.Engine = new Engine("01", 200, 4);

            //Create a new truck object using the default constructor
            Truck truck1 = new Truck();
            truck1.UID = "truck101";
            truck1.Make = "Ford";
            truck1.Model = "F-150";
            truck1.Year = 2021;
            truck1.PayloadCapacity = 1500;
            truck1.TowCapacity = 5000;
            truck1.NumWheels = 4;
            truck1.Engine = new Engine("03", 400, 8);
            Console.WriteLine("\nTest Car Clone");
            Console.WriteLine("==============");
            Car cloneCar = (Car) car1.Clone();
            Console.WriteLine(car1);
            Console.WriteLine("\t" + car1.Engine);
            Console.WriteLine(cloneCar);
            Console.WriteLine("\t" + cloneCar.Engine);
            Console.WriteLine("Change car1.Transmission and car1.Engine.Horsepower");
            car1.Transmission = "automatic";
            car1.Engine.Horsepower = 1000;
            Console.WriteLine(car1);
            Console.WriteLine("\t" + car1.Engine);
            Console.WriteLine(cloneCar);
            Console.WriteLine("\t" + cloneCar.Engine);
            Console.WriteLine("\nTest Truck Clone");
            Console.WriteLine("=================");
            Truck cloneTruck = (Truck) truck1.Clone();
            Console.WriteLine(truck1);
            Console.WriteLine("\t" + truck1.Engine);
            Console.WriteLine(cloneTruck);
            Console.WriteLine("Change truck1.TowCapacity and truck1.Engine.Horsepower");
            truck1.TowCapacity = 2000;
            truck1.Engine.Horsepower = 1000;
            Console.WriteLine(truck1);
            Console.WriteLine("\t" + truck1.Engine);
            Console.WriteLine(cloneTruck);
            Console.WriteLine("\t" + cloneTruck.Engine);





        }
    }
}

