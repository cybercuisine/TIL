
use rocket_okapi::openapi;
use rocket::serde::json::Json;

use crate::types::hello::Hello;
use crate::my_error::my_error::MyError;

#[openapi(tag = "Hello")]
#[post("/hello", data = "<message>")]
pub fn hello(message: &str) -> Result<Json<Hello>, MyError> {
    let response = Hello {
        message: message.to_string(),
    };
    Ok(Json(response))
}