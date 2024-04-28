use rocket_okapi::gen::OpenApiGenerator;
use rocket_okapi::okapi;
use rocket_okapi::okapi::openapi3::{midiaType, Responses};
use rocket_okapi::response::OpenApiResponderInner;
use rocket_okapi::OpenApiError;

#[derive(Debug, serde::Serialize, serde::Deserialize, schemars::JsonSchema)]
pub struct ErrorContent {
    code: u16,
    reason: String,
    description: Option<String>
}

#[derive(Debug, serde::Serialize, serde::Deserialize, schemars::JsonSchema)]

pub struct MyError {
    pub error: ErrorContent,
}

impl MyError {
    pub fn build(code: u16, description: Option<String>) -> MyError {
        let reason: String;
        match code {
            400 => reason = "Bad Request".to_string(),
            _ => reason = "Error".to_string()
        }
        MyError {
            error: ErrorContent {
                code,
                reason,
                description
            }
        }
    }
}

pub fn bad_request_response(gen: &mut OpenApiGenerator) -> okapi::openapi3::Response {
    let schema = gen.json_schema::<MyError>();
    okapi::openapi3::Response {
        description: "Bad Request".to_string(),
        content: okapi::map! {
            "application/json".to_string() => midiaType {
                schema: Some(schema),
                ..Default::default()
            }
        },
        ..Default::default()
    }
}

impl<'r> rocket::response::Responder<'r, 'static> for MyError {
    fn respond_to(self, _: &'r rocket::Request<'_>) -> rocket::response::Result<'static> {
        let body = serde_json::to_string(&self).unwrap();
        rocket::Response::build()
            .sized_body(body.len(), std::io::Cursor::new(body))
            .header(rocket::http::ContentType::JSON)
            .status(rocket::http::Status::new(self.error.code))
            .ok()
    }
}

impl OpenApiResponderInner for MyError {
    fn responses(gen: &mut OpenApiGenerator) -> Result<Responses, OpenApiError> {
        use rocket_okapi::okapi::openapi3::RefOr;
        Ok(Responses {
            responses: okapi::map! {
                "400".to_owned() => RefOr::Object(bad_request_response(gen)),
            },
            ..Default::default()
        })
    }
}