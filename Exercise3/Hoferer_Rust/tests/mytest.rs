use adlib::*;

#[test]
fn first_test() {
    let mut lifty = reset_lift();
    assert_eq!(get_lift_position(lifty), 0);
    lifty = call_lift_to_pos(&lifty, 2);
    assert_eq!(get_lift_position(lifty), 2);
}