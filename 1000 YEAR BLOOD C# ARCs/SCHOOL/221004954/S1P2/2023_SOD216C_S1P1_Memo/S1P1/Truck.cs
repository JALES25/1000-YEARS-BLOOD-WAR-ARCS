// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Class Truck. Represent a Truck object; Inherits from Vehicle

using System;

namespace S1P1
{
    public class Truck : Vehicle, ICloneable    
    {

        //
        //Name             : PayloadCapacity
        //Purpose          : Gets or sets the paylaod capacity of the truck.
        //Re-use           : None
        //Method Parameters: int - the new value for PayloadCapacity.
        //Output Type      : int - the value for PayloadCapacity.
        //
        public int PayloadCapacity { get; set; } //end property

        //
        //Name             : TowCapacity
        //Purpose          : Gets or sets the tow capacity of the truck.
        //Re-use           : None
        //Method Parameters: int - the new value for TowCapacity.
        //Output Type      : int - the value for TowCapacity.
        //
        public int TowCapacity { get; set; } //end property

        //
        //Name             : NumWheels
        //Purpose          : Gets or sets the number of wheels of the truck.
        //Re-use           : None
        //Method Parameters: int - the new value for NumWheels.
        //Output Type      : int - the value for NumWheels.
        //
        public int NumWheels { get; set; } //end property

        //
        // Name             : Truck()
        // Purpose          : Initializes a new instance of the Truck class with default property values.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : None
        //
        public Truck()
        {
        } // end method

        //
        // Name             : Truck(string UID, string make, string model, int year,
        //                        int payloadCapacity, int towCapacity, int numWheels, Engine engine)
        // Purpose          : Initializes a new instance of the Truck class with method parameter values.
        // Re-use           : None
        // Method Parameters:
        //  - string UID - The unique identifier of the truck.
        //  - string make - The make of the truck.
        //  - string model - The model of the truck.
        //  - int year - The year of the truck.
        //  - int payloadCapacity - The payload capacity of the truck
        //  - int towCapacity - The tow capacity of the truck
        //  - int numWheels - The number of wheels of the truck.
        //  - Engine engine - The engine of the truck.
        // Output Type      : None
        //
        public Truck(string UID, string make, string model, int year,
            int payloadCapacity, int towCapacity, int numWheels, Engine engine)
        {

            this.UID = UID;
            Make = make;
            Model = model;
            Year = year;
            PayloadCapacity = payloadCapacity;
            TowCapacity = towCapacity;
            NumWheels = numWheels;
            //Engine = engine;
            //
            /* checks if engine is NULL it then instantiate Engine with the default constructor
              * & if engine is NOT NULL then instantiates Engine with the appropriate constructor
              */
            Engine = engine != null ? new Engine(engine.NumberCylinders ,engine.Horsepower, engine.FuelType) : new Engine();
            //
            
        } // end method




        //
        // Name             : object Clone()
        // Purpose          : Returns a new Truck object that is a copy of the current instance.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : object
        //                    - A new Truck object that is a copy of this instance.
        //

        // Implementation of ICloneable interface
        public object Clone()
        {
            // Create new Truck object and set properties
            Truck newTruck = new Truck();
            newTruck.UID = this.UID;
            newTruck.Make = this.Make;
            newTruck.Model = this.Model;
            newTruck.Year = this.Year;
            newTruck.PayloadCapacity = this.PayloadCapacity;
            newTruck.TowCapacity = this.TowCapacity;
            newTruck.NumWheels = this.NumWheels;

            // Instantiate new Engine object based on existing Engine object
            newTruck.Engine = new Engine(this.Engine.NumberCylinders, this.Engine.Horsepower, this.Engine.FuelType);
            //
            // Store cloned instance in cloneTruck variable
            //
            // Return new Truck object
            return newTruck;
        }


        //
        // Name             : string ToString()
        // Purpose          : Returns a string representation of the Truck object.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : string
        //                    - A string representation of the Truck object.
        //
        //

        //


        public override string ToString()
        {
            return $"PayloadCapacity: {PayloadCapacity}, TowCapacity: {TowCapacity}, " +
                $"NumWheels: {NumWheels}";
        } // end method
    } // end class
} // end namespace

