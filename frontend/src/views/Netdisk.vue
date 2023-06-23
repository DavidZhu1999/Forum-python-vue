<template>
  <div id="netdisk">
    <v-container style="display: flex; justify-content: space-around"
      ><h1>NetDisk</h1></v-container
    >
    <v-divider></v-divider>
    <v-card max-width="1000px" style="margin: 0px auto">
      <v-toolbar color="light-blue" dark>
        <v-btn color="primary" style="margin-right: 50px">upload</v-btn>

        <v-btn color="success">New Folder</v-btn>

        <v-spacer></v-spacer>

        <v-text-field
          style="padding-top: 25px"
          v-model="first"
          label="Search"
          dense
          outlined
          @keyup.enter="tishi()"
        ></v-text-field>

        <v-btn icon @click="tishi()">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-toolbar>

      <v-container class="grey lighten-5">
        <v-row v-for="(item, i) in items" :key="i" no-gutters>
          <v-col cols="5">
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-col>
          <v-col cols="3">
            <v-list-item-title v-text="item.type"></v-list-item-title>
          </v-col>
          <v-col cols="3">
            <v-list-item-title v-text="item.big"></v-list-item-title>
          </v-col>
          <v-col cols="1" style="text-align:right">
            <v-icon v-show="item.type != 'folder'" @click="tishi(item.big)"
              >mdi-cloud-download-outline</v-icon
            >
            <v-icon>mdi-trash-can-outline</v-icon>
          </v-col>
        </v-row>
      </v-container>
      
      <v-alert
      :value="alert"
      color="pink"
      dark
      border="top"
      icon="mdi-home"
      transition="scale-transition"
    >
Phasellus tempus. Fusce ac felis sit amet ligula pharetra condimentum. In dui magna, posuere eget, vestibulum et, tempor auctor, justo. Pellentesque posuere. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo.

      Phasellus nec sem in justo pellentesque facilisis. Phasellus magna. Cras risus ipsum, faucibus ut, ullamcorper id, varius ac, leo. In hac habitasse platea dictumst. Praesent turpis.
    </v-alert>
      <!-- <v-list dense>
        <v-list-item v-for="(item, i) in items" :key="i">
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
          <v-spacer></v-spacer>
          <v-list-jitem-content>
            <v-list-item-title v-text="item.type"></v-list-item-title>
          </v-list-jitem-content>
          <v-spacer></v-spacer>
          <v-list-jitem-content>
            <v-list-item-title v-text="item.big"></v-list-item-title>
          </v-list-jitem-content>
          <v-list-item-icon>
            <v-icon v-show="item.type != 'folder'" @click="tishi(item.big)"
              >mdi-cloud-download-outline</v-icon
            >
            <v-icon>mdi-trash-can-outline</v-icon>
          </v-list-item-icon>
        </v-list-item>

        <v-subheader>REPORTS</v-subheader>
      <v-list-item-group
        v-model="selectedItem"
        color="primary"
      >
        <v-list-item
          v-for="(item, i) in items"
          :key="i"
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon"></v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
      </v-list> -->
    </v-card>
  </div>
</template>

<script>
export default {
  data: () => ({
    first:"",
    alert:false,
    items: [
      { text: "folder", type: "folder" },
      { text: "My Files", type: "txt", big: "80mb" },
      { text: "Shared with me", type: ".mdi", big: "801mb" },
      { text: "Starred", type: ".exe", big: "380mb" },
      { text: "Recent", type: ".word", big: "80mb" },
      { text: "Offline", type: ".ppt", big: "2.333mb" },
      { text: "Uploads", type: ".c", big: "80mb" },
      { text: "Backups", type: ".py", big: "80mb" },
    ],
    
  }),
  methods: {
    tishi: function (big) {
      alert(big);
    },
  },
  mounted:function(){
    if(this.$store.state.quanjulogin == 'true'){

    }
    else{
      this.alert = true
    }
  }
};
</script>