// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Class Vehicle. Represent a Vehicle object; Has an Engine object; Implements the IUniqueID interface


using System;

namespace S1P1
{
    public class Vehicle : IUniqueID
    {
        //
        //Name              : Make
        //Purpose           : Gets or sets the make of the vehicle.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for Make
        //Output Type       : string
        //                    - value of Make
        //
        public string Make { get; set; }// end property 

        //
        //Name              : Model
        //Purpose           : Gets or sets the model of the vehicle.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for Model
        //Output Type       : string
        //                    - value of Model
        //
        public string Model { get; set; }

        //
        //Name              : Year
        //Purpose           : Gets or sets the year of the vehicle.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for Year
        //Output Type       : string
        //                    - value of Year
        //
        public int Year { get; set; }// end property

        //
        //Name              : Engine
        //Purpose           : Gets or sets the Engine object of the vehicle.
        //Re-use            : None
        //Method Parameters : Engine
        //                    - new value for Engine
        //Output Type       : Engine
        //                    - value of Engine
        //
        public Engine Engine { get; set; } // end property

        //
        //Name              : UID
        //Purpose           : Gets or sets the UID of the vehicle.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for UID
        //Output Type       : string
        //                    - value of UID
        //
        public string UID { get; set; } // end property

        //
        // Name             : Vehicle()
        // Purpose          : Initializes a new instance of the Vehicle class with default property values.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : None
        //
        public Vehicle()
        {
        } // end method

        //
        // Name             : Vehicle(string UID, string make, string model, int year, Engine engine)
        // Purpose          : Initializes a new instance of the Vehicle class with specified property values.
        // Re-use           : None
        // Method Parameters:
        //  - string UID - The unique id for the vehicle.
        //  - string make - The make of the vehicle.
        //  - string model - The model of the vehicle.
        //  - int year - The year of the vehicle.
        //  - Engine engine - The composed Engine object of the Vehicle object
        // Output Type: None
        //
        public Vehicle(string UID, string make, string model, int year, Engine engine)
        {
            this.UID = UID;
            Make = make;
            Model = model;
            Year = year;
            Engine = engine != null ? new Engine(engine.Horsepower, engine.CylinderCount) : new Engine();
            //Ternary operator -- if engine is NOT NULL, intatiates engine with APPROPRIATE constructor & if NULL
            // & if NULL instatiate engine with default constructor*/
        } // end method

        //
        // Name             : string ToString()
        // Purpose          : Returns a string representation of the Vehicle object.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : string
        //                    - A string representation of the Vehicle object.
        //
        public override string ToString()
        {
            return $"UID: {UID}, Make: {Make}, Model: {Model}, Year: {Year}";
        } // end method

        //
        //Name              : string UIDString()
        //Purpose           : Returns a string representation of the unique identifier of the vehicle.
        //Re-use            : None
        //Method Parameters : None
        //Output Type       : string
        //                    - a string representation of the unique identifier of the vehicle.
        //
        public string UIDString()
        {
            return UID;
        } // end method
    } // end class
} // end namespace

