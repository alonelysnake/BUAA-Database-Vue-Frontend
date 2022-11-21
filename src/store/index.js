import { createStore } from 'vuex'

export default createStore({

    state: {
        loggedIn: false,
        searchItem: "",
        user: {
            nickname: "DefaultNickname",
            userID: 'DefaultUsername',
            type:1,
            // 头像Url
            avatar: "",
        }
    },

    mutations: {
        login(state,data) {
            state.loggedIn = true;
            state.user.username = data.username;
            state.user.userID = data.userID;
            state.user.avatar = data.avatar;
        },
        logout(state) {
            state.loggedIn = false;
            state.user.username = '';
        },
        setAvatarUrl(state, data) {
            state.user.avatar = data.avatar;
        },
        setInfo(state, data) {
            state.user.nickname = data.nickname;
        }
    },
    actions: {
    },
    modules: {
    }
})
