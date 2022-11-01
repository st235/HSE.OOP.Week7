import streamlit as st


class StreamlitDict(dict):
    """
    Streamlit override of Python's dict.
    Unordered hash dictionary that supports persistent storage.
    """

    def __init__(self, title: str, new_dict: dict = None):
        super().__init__()

        self.__title = title

        if new_dict is None:
            self.__inner_dict = dict()
            if self.__title in st.session_state and type(st.session_state[self.__title]) is dict:
                self.__inner_dict = st.session_state[self.__title]
        else:
            self.__inner_dict = new_dict
            st.session_state[self.__title] = self.__inner_dict

    def __setitem__(self, key, item):
        self.__inner_dict[key] = item
        st.session_state[self.__title] = self.__inner_dict

    def __getitem__(self, key):
        return self.__inner_dict[key]

    def __repr__(self):
        return repr(self.__inner_dict)

    def __len__(self):
        return len(self.__inner_dict)

    def __delitem__(self, key):
        del self.__inner_dict[key]
        st.session_state[self.__title] = self.__inner_dict

    def clear(self):
        result = self.__inner_dict.clear()
        st.session_state[self.__title] = self.__inner_dict
        return result

    def copy(self):
        return StreamlitDict(self.__title, self.__inner_dict)

    def has_key(self, k):
        return k in self.__inner_dict

    def update(self, *args, **kwargs):
        result = self.__inner_dict.update(*args, **kwargs)
        st.session_state[self.__title] = self.__inner_dict
        return result

    def keys(self):
        return self.__inner_dict.keys()

    def values(self):
        return self.__inner_dict.values()

    def items(self):
        return self.__inner_dict.items()

    def pop(self, *args):
        result = self.__inner_dict.pop(*args)
        st.session_state[self.__title] = self.__inner_dict
        return result

    def __contains__(self, item):
        return item in self.__inner_dict

    def __iter__(self):
        return iter(self.__inner_dict)
