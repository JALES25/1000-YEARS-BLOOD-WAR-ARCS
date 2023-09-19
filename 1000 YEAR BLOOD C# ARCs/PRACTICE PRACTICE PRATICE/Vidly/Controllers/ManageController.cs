using Microsoft.AspNetCore.Mvc;

namespace Vidly.Controllers
{
    public class ManageController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
    }
}
