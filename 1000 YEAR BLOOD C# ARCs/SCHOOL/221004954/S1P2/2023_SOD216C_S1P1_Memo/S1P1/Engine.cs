// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Class Engine. Represent a Engine object; Implements the IUniqueID interface

using System;

namespace S1P1
{
    public class Engine : IUniqueID, ICloneable
    {

        //______________________________________________________________________________
        // Name             : NumberCylinders
        // Purpose          : Gets or sets the NumberCylinders of the engine.
        // Re-use           : None
        // Method Parameters: int
        //                    - new value for NumberCylinders
        // Output Type      : int - The NumberCylinders of the engine.
        public int NumberCylinders { get; set; } //end property

        // Name             : FuelType
        // Purpose          : Gets or sets the FuelType of the engine.
        // Re-use           : None
        // Method Parameters: int
        //                    - new value for FuelType
        // Output Type      : int - The FuelType of the engine.
        public int FuelType { get; set; } //end property
        //______________________________________________________________________________
        // Name             : Horsepower
        // Purpose          : Gets or sets the horsepower of the engine.
        // Re-use           : None
        // Method Parameters: int
        //                    - new value for Horsepower
        // Output Type      : int - The Horsepower of the engine.
        public int Horsepower { get; set; } //end property

        // Name             : CylinderCount
        // Purpose          : Gets or sets the CylinderCount of the engine.
        // Re-use           : None
        // Method Parameters: int
        //                    - new value for CylinderCount
        // Output Type      : int - The CylinderCount of the engine.
        public int CylinderCount { get; set; } //end property

        //
        //Name              : UID
        //Purpose           : Gets or sets the UID of the Engine.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for UID
        //Output Type       : string
        //                    - value of UID
        public string UID { get; set; } //end property

        //
        // Name             : Engine()
        // Purpose          : Initializes a new instance of the Engine class with default property values.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : None
        //
        public Engine()
        {
        } // end method

        //
        // Name             : Engine(string UID, int horsepower, int cylinderCount)
        // Purpose          : Creates a new instance of the Engine class with the specified unique identifier, horsepower, and cylinder count.
        // Re-use           : None
        // Method Parameters:
        // - string UID: The unique identifier string for the engine.
        // - int horsepower: The horsepower of the engine.
        // - int cylinderCount: The cylinder count of the engine.
        // Output Type      : None
        //
        public Engine(string UID, int horsepower, int cylinderCount, int fueltype, int numbercylinders)
        {
            this.UID = UID;
            Horsepower = horsepower;
            CylinderCount = cylinderCount;
            FuelType = fueltype;
            NumberCylinders = numbercylinders;
        }
        // end method

        //
        public object Clone()
        {
            return new Engine(this.NumberCylinders, this.Horsepower, this.FuelType);
        }
        //


        //
        // Name             : string ToString()
        // Purpose          : Returns a string representation of the Engine object.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : string
        //                    - A string representation of the Engine object.
        //
        public override string ToString()
        {
            return $"Horsepower: {Horsepower}, CylinderCount: {CylinderCount}";
        } // end method

        //
        //Name              : string UIDString()
        //Purpose           : Returns a string representation of the unique identifier of the Engine.
        //Re-use            : None
        //Method Parameters : None
        //Output Type       : string
        //                    - a string representation of the unique identifier of the Engine.
        //
        public string UIDString()
        {
            return UID;
        } // end method
    } // end class
} // end namespace

