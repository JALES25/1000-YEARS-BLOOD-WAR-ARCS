// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Class Car. Represent a Car object; Inherits from Vehicle

using System;

namespace S1P1
{
    public class Car : Vehicle, ICloneable
    {

        private string transmission;

        //
        //Name             : NumDoors
        //Purpose          : Gets or sets the number of doors of the car.
        //Re-use           : None
        //Method Parameters: int - the new value for NumDoors.
        //Output Type      : int - the value for NumDoors.
        //
        public int NumDoors { get; set; } //end property

        //
        //Name             : BodyStyle
        //Purpose          : Gets or sets the body style of the car.
        //Re-use           : None
        //Method Parameters: string - the new value for BodyStyle.
        //Output Type      : string - the value for BodyStyle.
        //
        public string BodyStyle { get; set; } //end property

        //
        //Name             : Transmission
        //Purpose          : Gets or sets the transmission of the car.
        //                   If the value is not "automatic", the transmission type will be set to "manual".
        //Re-use           : None
        //Method Parameters: string - the new value for transmission.
        //Output Type      : string - the value for transmission.
        //
        public string Transmission
        {
            get
            {
                return transmission;
            } // end get
            set
            {
                if (value == "automatic")
                {
                    transmission = value;
                } // end if
                else
                {
                    transmission = "manual";
                } // end else
            } // end set
        } //end property

        //
        // Name             : Car()
        // Purpose          : Initializes a new instance of the Car class with default property values.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : None
        //
        public Car()
        {
        } // end method


        //
        // Name             : Car(string UID, string make, string model, int year, int numDoors, string bodyStyle, Engine engine)
        // Purpose          : Initializes a new instance of the Car class with method parameter values.
        // Re-use           : None
        // Method Parameters:
        //  - string UID - The unique identifier of the car.
        //  - string make - The make of the car.
        //  - string model - The model of the car.
        //  - int year - The year of the car.
        //  - int numDoors - The number of doors of the car.
        //  - string bodyStyle - The body style of the car.
        //  - Engine engine - The engine of the car.
        // Output Type      : None
        //
        public Car(string UID, string make, string model, int year, int numDoors, string bodyStyle, Engine engine)
        {
            this.UID = UID;
            Make = make;
            Model = model;
            Year = year;
            NumDoors = numDoors;
            BodyStyle = bodyStyle;
            //Engine = engine;
            Engine = engine ?? new Engine(); //null-coalescing operator -- instantiate Engine with default constructor if engine is null 
            transmission = "manual";
        } // end method

        //
        // Name             : string ToString()
        // Purpose          : Returns a string representation of the Car object.
        // Re-use           : None
        // Method Parameters: None
        // Output Type      : string
        //                    - A string representation of the Car object.
        //
        public override string ToString()
        {
            return $"NumDoors: {NumDoors}, BodyStyle: {BodyStyle}, Transmission: {Transmission}";
        } // end method

        public object Clone()
        {
            return new Car(this.UID, this.Make, this.Model, this.Year, this.NumDoors, this.BodyStyle, this.Engine.Clone() as Engine);
        }// end method

    } // end class
} // end namespace


