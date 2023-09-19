using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
//using System.Web.Mvc;   DEPRECATED

using Vidly.Models;  //?

using Microsoft.AspNetCore.Mvc;

namespace Vidly.Controllers
{
    public class MoviesController : Controller
    {
        //GET Movies/Random
        public IActionResult Random()
        {
            var movie =  new Movie() {  Name = "Shrek!"};

            return View(movie);
        }
    }
}
