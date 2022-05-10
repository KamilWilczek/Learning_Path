import React from 'react';
import AppContext from '../../context';
import List from '../../components/List/List';

const ArticlesView = () => (
  <AppContext.Consumer>
    {(value) => (
      // <p>This is an Articles View {context}</p>
      <List items={value.article}/>
    )}

  </AppContext.Consumer>
);

export default ArticlesView;