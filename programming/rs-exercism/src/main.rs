// The code below is a stub. Just enough to satisfy the compiler.
// In order to pass the tests you can add-to or change any of this code.

const EARTH_YEAR_SECONDS: f64 = 31_557_600.0;
const MERCURY_YEAR_RATIO: f64 = 0.2408467;
const VENUS_YEAR_RATIO: f64 = 0.61519726;
const MARS_YEAR_RATIO: f64 = 1.8808158;
const JUPITER_YEAR_RATIO: f64 = 11.862615;
const SATURN_YEAR_RATIO: f64 = 29.447498;
const URANUS_YEAR_RATIO: f64 = 84.016846;
const NEPTUNE_YEAR_RATIO: f64 = 164.79132;

#[derive(Debug)]
pub struct Duration(u64);

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Duration(s)
    }
}

pub trait Planet {
    fn years_during(d: &Duration) -> f64;
}

macro_rules! impl_planet {
    ($planet:ident, $year_ratio:expr) => {
        pub struct $planet;

        impl Planet for $planet {
            fn years_during(d: &Duration) -> f64 {
                d.0 as f64 / EARTH_YEAR_SECONDS / $year_ratio
            }
        }
    };
}



impl_planet!(Mercury, MERCURY_YEAR_RATIO);
impl_planet!(Venus, VENUS_YEAR_RATIO);
impl_planet!(Earth, 1.0);
impl_planet!(Mars, MARS_YEAR_RATIO);
impl_planet!(Jupiter, JUPITER_YEAR_RATIO);
impl_planet!(Saturn, SATURN_YEAR_RATIO);
impl_planet!(Uranus, URANUS_YEAR_RATIO);
impl_planet!(Neptune, NEPTUNE_YEAR_RATIO);


fn main() {}

fn assert_in_delta(expected: f64, actual: f64) {
    let diff: f64 = (expected - actual).abs();
    let delta: f64 = 0.01;
    if diff > delta {
        panic!("Your result of {actual} should be within {delta} of the expected result {expected}")
    }
}
#[test]
fn age_on_earth() {
    let seconds = 1000000000;
    let duration = Duration::from(seconds);
    let output = Earth::years_during(&duration);
    let expected = 31.69;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_mercury() {
    let seconds = 2134835688;
    let duration = Duration::from(seconds);
    let output = Mercury::years_during(&duration);
    let expected = 280.88;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_venus() {
    let seconds = 189839836;
    let duration = Duration::from(seconds);
    let output = Venus::years_during(&duration);
    let expected = 9.78;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_mars() {
    let seconds = 2129871239;
    let duration = Duration::from(seconds);
    let output = Mars::years_during(&duration);
    let expected = 35.88;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_jupiter() {
    let seconds = 901876382;
    let duration = Duration::from(seconds);
    let output = Jupiter::years_during(&duration);
    let expected = 2.41;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_saturn() {
    let seconds = 2000000000;
    let duration = Duration::from(seconds);
    let output = Saturn::years_during(&duration);
    let expected = 2.15;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_uranus() {
    let seconds = 1210123456;
    let duration = Duration::from(seconds);
    let output = Uranus::years_during(&duration);
    let expected = 0.46;
    assert_in_delta(expected, output);
}
#[test]
fn age_on_neptune() {
    let seconds = 1821023456;
    let duration = Duration::from(seconds);
    let output = Neptune::years_during(&duration);
    let expected = 0.35;
    assert_in_delta(expected, output);
}
