import React from 'react';
import AppContext from '../../context';
import List from '../../components/List/List';

const TwittersView = () => (
  <AppContext.Consumer>
    {(value) => (
      <List items={value.twitter}/>
    )}

  </AppContext.Consumer>
);

export default TwittersView;