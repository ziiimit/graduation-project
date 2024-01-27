import Cookie from 'js-cookie';

const state = {
    sidebar: {
        opened: Cookie.get('sidebarStatus') ? !!+Cookie.get('sidebarStatus') : true,
        withAnimation: false,
    },
    device: 'desktop',
    mode: Cookie.get('mode') ? Cookie.get('mode') : 'dark'
}

const mutations = {
    CLOSE_SIDEBAR: (state, withAnimation) => {
        state.sidebar.opened = false;
        state.sidebar.withAnimation = withAnimation;
    },
    TOGGLE_SIDEBAR: (state, withAnimation) => {
        state.sidebar.opened = !state.sidebar.opened;
        state.sidebar.withAnimation = withAnimation;
        Cookie.set('sidebarStatus', state.sidebar.opened ? '1' : '0');
    },
    SET_DEVICE: (state, device) => {
        state.device = device;
    },
    TOGGLE_MODE: (state) => {
        if (state.mode === 'dark') {
            state.mode = 'light';
            document.body.classList.replace("darkMode", 'lightMode');
        } else {
            state.mode = 'dark';
            document.body.classList.replace('lightMode', 'darkMode');
        }
        Cookie.set('mode', state.mode);
    }
}

const actions = {
    closeSidebar({ commit }, { withAnimation }) {
        commit('CLOSE_SIDEBAR', withAnimation);
    },
    toggleSidebar({ commit }, { withAnimation }) {
        commit('TOGGLE_SIDEBAR', withAnimation);
    },
    setDevice({ commit }, device) {
        commit('SET_DEVICE', device);
    },
    toggleMode({ commit }) {
        commit('TOGGLE_MODE');
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
}