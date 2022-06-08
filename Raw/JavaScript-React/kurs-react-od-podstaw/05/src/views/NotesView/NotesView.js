import React from 'react';
import AppContext from '../../context';
import List from '../../components/List/List';

const NotesView = () => (
  <AppContext.Consumer>
    {(value) => (
      <List items={value.note}/>
    )}

  </AppContext.Consumer>
);

export default NotesView;