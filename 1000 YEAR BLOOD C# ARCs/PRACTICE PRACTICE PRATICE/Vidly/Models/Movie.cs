using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace Vidly.Models
{
    // Plain old CLR object (POCO)
    // It represents the state and behavior of our application in terms of its problem domain
    // INn this case it does't have any behavior or logic it just has properties which we use for representing state
    public class Movie 
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }
}
