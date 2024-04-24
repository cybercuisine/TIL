use serde::Serialize;
use schemars::JsonSchema;

#[derive(Serialize, JsonSchema)]
pub struct Hello {
    pub message: String
}