namespace py user_profile
namespace java user_profile
struct User {
  1: i32 id,
  2: string name,
  3: optional string email
  4: optional string phone_number
}

service UserProfileService {
  User getUserById(1: i32 id)
}
