// Programmer name : P Kruger
// Student nr : 221004954
// Assignment nr : S1P2
// Purpose : Interface IUniqueID. Represent a unique ID.

using System;

namespace S1P1
{
    public interface IUniqueID
    {
        //
        //Name              : UID
        //Purpose           : Gets or sets a unique identifier string for the object.
        //Re-use            : None
        //Method Parameters : string
        //                    - new value for UID
        //Output Type       : string
        //                    - value of UID
        //
        string UID { get; set; } //end property

        //
        //Name              : string UIDString()
        //Purpose           : Returns a string representation of the unique identifier of the object.
        //Re-use            : None
        //Method Parameters : None
        //Output Type       : string
        //                    - a string representation of the unique identifier of the object.
        //
        string UIDString();
    } // end interface
} // end namespace

