#[derive(Default)]
pub struct Lift {
    floor: i32
}

impl Lift {
    fn get_lift_position(&self) -> &i32 { &self.floor }
}

pub fn reset_lift() -> Lift {
    println!("Lifty is in start position at floor 0!");
    Lift { floor: 0 }
}

pub fn call_lift_to_pos(pos: i32) {
    println!("Lifty got your call! Moving ...");
    l = move_lift_to_floor(l, pos);
    println!("Lifty moved to floor {}!", pos);
}

fn move_lift_to_floor(mut l: Lift, pos: i32) -> Lift {
    l.floor = pos;
    l
}
