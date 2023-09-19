using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace S1P1
{


    public interface IUniqueID
    {
        string UID { get; set; }
        string UIDString();
    }

    /*
    public class UniqueID : IUniqueID
    {
        private string uid;

        public UniqueID()
        {
            uid = Guid.NewGuid().ToString();
        }


        public sting UID
        {
            get { return uid; }
        }

        public string UIDString()
        {
            return uid;
        }

    }
    */

    public class Engine : IUniqueID
    {
        public int Horsepower { get; set; }
        public int CylinderCount { get; set; }
        public string UID { get; set; }

        public Engine() : this(0,0)
        {
           //ID = Guid.NewGuid().ToString();
        }

        public Engine(int horsepower, int cylinderCount) // this()
        {
            Horsepower = horsepower;
            CylinderCount = cylinderCount;
            UID = Guild.NewGuild().ToString();
        }

        public override string ToString()
        {
            return $"Horsepower : {Horsepower} \nCylinderCount: {CylinderCount}";
        }

        public string UIDString()
        {
            return UID;
        }

    }

    //_________________________________________________________________________________________

    public class Vehicle : IUniqueID
    {
        public string Make { get; set; }
        public string Model { get; set; }
        public int Year { get; set; }
        public string UID { get; private set; }

        public Vehicle() : this("", "", 0)
        {
            //UID = Guid.NewGuid().ToString();
        }

        public Vehicle(string make, string model, int year) //: this()
        {
            Make = make;
            Model = model;
            Year = year;
            UID = Guid.NewGuid().ToString();
        }

        public override string ToString()
        {
            return $"UID: {UID} \nMake: {Make} \nModel: {Model} \nYear: {Year}";
        }

        public string UIDString()
        {
            return UID;
        }
    }

    //_________________________________________________________________________________________

    public class Car : Vehicle
    {
        public int NumDoors { get; set; }
        public string BodyStyle { get; set; }
        public string Transmission { get; set; }

        public Car : this("", "", 0, 0, "","manual") 
        {
            //Transmission = "manual";  
        }

        public Car(string make, string model, int year, int numDoors, string bodyStyle, string transmission "manual") : base(make, model, year,)
        {
            numDoors = numDoors;
            bodyStyle = bodyStyle;
            Transmission = transmission;
        }

        public override string ToString()
        {
            return $"NumDoors: {NumDoors} \nBodyStyle: {BodyStyle} \nTransmission: {Transmission}";
        }
    }

    //_________________________________________________________________________________________

    public class Truck : Vehicle
    {
        public double PayloadCapacity { get; set; }
        public double TowCapacity { get; set; }
        public double NumWheels { get; set; } 

        public Truck() : this(""."",0, 0, 0, 0) //base()
        {

        }

        public Truck(string make, string model, int year, double payloadCapacity, double towCapacity, int numWheels) : base(make, model, year)
        {
            PayloadCapacity = payloadCapacity;
            TowCapacity = towCapacity;
            NumWheels = numWheels;
        }

        public override string ToString()
        {
            return $"PayloadCapacity: {PayloadCapacity} \n TowCapacity: {TowCapacity} \nNumwheels: {NumWheels}";
        }
    }

    //_________________________________________________________________________________________
    //_________________________________________________________________________________________
    //_________________________________________________________________________________________

    internal class Program
    {
        static void Main(string[] args)
        {
        }
    }
}
