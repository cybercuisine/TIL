#[macro_use]
extern crate rocket;

use dotenv::dotenv;
use rocket_okapi::openapi_get_routes;

mod controller;
mod types;
mod my_error;

#[launch]
fn rocket() -> _ {
    dotenv().ok();
    rocket::build()
    .mount(
        "/",
        openapi_get_routes![
            controller::hello::hello
        ]
    )
}
