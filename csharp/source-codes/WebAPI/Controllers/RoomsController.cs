using System;
using Microsoft.AspNetCore.Mvc;


namespace WebAPI.Controllers
{
    [ApiController]
    [Route("/[controller]")]
    public class RoomsController : ControllerBase
    {
        [HttpGet(Name = "[controller]_[action]")]
        public IActionResult Index()
        {
            throw new NotImplementedException();
        }
    }
}