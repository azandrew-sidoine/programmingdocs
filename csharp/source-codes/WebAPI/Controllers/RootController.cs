using System;
using Microsoft.AspNetCore.Mvc;


namespace WebAPI.Controllers
{
    // Web API root controller
    [ApiController]
    [Route("/")]
    public class RootController : ControllerBase
    {
        [HttpGet(Name = nameof(RootController.Index))]
        public IActionResult Index()
        {
            return Ok(new {
                href = Url.Link(nameof(RootController.Index), null),
                rooms = new {
                    href = Url.Link("rooms_index", null),
                }
            });
        }
    }
}