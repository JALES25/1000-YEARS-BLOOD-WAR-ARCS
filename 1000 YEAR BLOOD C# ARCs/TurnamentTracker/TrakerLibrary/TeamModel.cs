using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Web;

namespace TrakerLibrary
{
    public class TeamModel
    {
        public List<PersonModel> TeamMembers { get; set; } // = new List<Person>();        new way to  have constructures
        public string TeamName { get; set; }

        public TeamModel()
        {
            TeamMembers = new List<PersonModel>();
        }



    }
}
