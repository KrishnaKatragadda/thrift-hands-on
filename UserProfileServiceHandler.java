package user.profile;

import java.util.HashMap;
import java.util.Map;

public class UserProfileServiceHandler implements UserProfileService.Iface {
    private Map<Integer, User> users = new HashMap<>();

    public UserProfileServiceHandler() {
        users.put(1, new User(1, "Alice", "alice@example.com"));
        users.put(2, new User(2, "Bob"));
    }

    @Override
    public User getUserById(int id) {
        return users.getOrDefault(id, new User(id, "Unknown"));
    }
}
